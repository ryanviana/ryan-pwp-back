import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { CreateEducationDto } from './dto/create-education.dto';
import { UpdateEducationDto } from './dto/update-education.dto';
import { Education, EducationDocument } from './entities/education.entity';

@Injectable()
export class EducationService {
  constructor(
    @InjectModel(Education.name)
    private educationModel: Model<EducationDocument>,
  ) {}

  async create(createEducationDto: CreateEducationDto): Promise<Education> {
    const createdEducation = new this.educationModel(createEducationDto);
    return createdEducation.save();
  }

  async findAll(): Promise<Education[]> {
    return this.educationModel.find().exec();
  }

  async findOne(id: string): Promise<Education> {
    const education = await this.educationModel.findById(id).exec();
    if (!education) {
      throw new NotFoundException(`Education with ID ${id} not found`);
    }
    return education;
  }

  async update(
    id: string,
    updateEducationDto: UpdateEducationDto,
  ): Promise<Education> {
    const updatedEducation = await this.educationModel
      .findByIdAndUpdate(id, updateEducationDto, { new: true })
      .exec();

    if (!updatedEducation) {
      throw new NotFoundException(`Education with ID ${id} not found`);
    }

    return updatedEducation;
  }

  async remove(id: string): Promise<Education> {
    const deletedEducation = await this.educationModel
      .findByIdAndDelete(id)
      .exec();

    if (!deletedEducation) {
      throw new NotFoundException(`Education with ID ${id} not found`);
    }

    return deletedEducation;
  }
}
