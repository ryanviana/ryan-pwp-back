import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateWorkExperienceDto } from './dto/create-work-experience.dto';
import { UpdateWorkExperienceDto } from './dto/update-work-experience.dto';
import {
  WorkExperience,
  WorkExperienceDocument,
} from './entities/work-experience.entity';

@Injectable()
export class WorkExperienceService {
  constructor(
    @InjectModel(WorkExperience.name)
    private workExperienceModel: Model<WorkExperienceDocument>,
  ) {}

  async create(
    createWorkExperienceDto: CreateWorkExperienceDto,
  ): Promise<WorkExperience> {
    const createdWorkExperience = new this.workExperienceModel(
      createWorkExperienceDto,
    );
    return createdWorkExperience.save();
  }

  async findAll(): Promise<WorkExperience[]> {
    return this.workExperienceModel.find().exec();
  }

  async findOne(id: string): Promise<WorkExperience> {
    const workExperience = await this.workExperienceModel.findById(id).exec();
    if (!workExperience) {
      throw new NotFoundException(`WorkExperience with ID ${id} not found`);
    }
    return workExperience;
  }

  async update(
    id: string,
    updateWorkExperienceDto: UpdateWorkExperienceDto,
  ): Promise<WorkExperience> {
    const updatedWorkExperience = await this.workExperienceModel
      .findByIdAndUpdate(id, updateWorkExperienceDto, { new: true })
      .exec();

    if (!updatedWorkExperience) {
      throw new NotFoundException(`WorkExperience with ID ${id} not found`);
    }

    return updatedWorkExperience;
  }

  async remove(id: string): Promise<WorkExperience> {
    const deletedWorkExperience = await this.workExperienceModel
      .findByIdAndDelete(id)
      .exec();

    if (!deletedWorkExperience) {
      throw new NotFoundException(`WorkExperience with ID ${id} not found`);
    }

    return deletedWorkExperience;
  }
}
