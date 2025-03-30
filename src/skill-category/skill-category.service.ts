import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateSkillCategoryDto } from './dto/create-skill-category.dto';
import { UpdateSkillCategoryDto } from './dto/update-skill-category.dto';
import {
  SkillCategory,
  SkillCategoryDocument,
} from './entities/skill-category.entity';

@Injectable()
export class SkillCategoryService {
  constructor(
    @InjectModel(SkillCategory.name)
    private skillCategoryModel: Model<SkillCategoryDocument>,
  ) {}

  async create(
    createSkillCategoryDto: CreateSkillCategoryDto,
  ): Promise<SkillCategory> {
    const createdSkillCategory = new this.skillCategoryModel(
      createSkillCategoryDto,
    );
    return createdSkillCategory.save();
  }

  async findAll(): Promise<SkillCategory[]> {
    return this.skillCategoryModel.find().exec();
  }

  async findOne(id: string): Promise<SkillCategory> {
    const skillCategory = await this.skillCategoryModel.findById(id).exec();
    if (!skillCategory) {
      throw new NotFoundException(`SkillCategory with ID ${id} not found`);
    }
    return skillCategory;
  }

  async update(
    id: string,
    updateSkillCategoryDto: UpdateSkillCategoryDto,
  ): Promise<SkillCategory> {
    const updatedSkillCategory = await this.skillCategoryModel
      .findByIdAndUpdate(id, updateSkillCategoryDto, { new: true })
      .exec();

    if (!updatedSkillCategory) {
      throw new NotFoundException(`SkillCategory with ID ${id} not found`);
    }

    return updatedSkillCategory;
  }

  async remove(id: string): Promise<SkillCategory> {
    const deletedSkillCategory = await this.skillCategoryModel
      .findByIdAndDelete(id)
      .exec();

    if (!deletedSkillCategory) {
      throw new NotFoundException(`SkillCategory with ID ${id} not found`);
    }

    return deletedSkillCategory;
  }
}
